#!/usr/bin/env node
/**
 * encrypt-data.mjs
 * AES-256-GCM encryption for strategic-data-unified.json
 * Usage: node scripts/encrypt-data.mjs <password>
 *    or: DATA_PASSWORD=<password> node scripts/encrypt-data.mjs
 */

import { createHash, pbkdf2Sync, randomBytes, createCipheriv } from 'crypto'
import { readFileSync, writeFileSync, copyFileSync } from 'fs'
import { fileURLToPath } from 'url'
import { dirname, join } from 'path'

const __dirname = dirname(fileURLToPath(import.meta.url))
const publicDir = join(__dirname, '..', 'public')

const INPUT_FILE   = join(publicDir, 'strategic-data-unified.json')
const OUTPUT_FILE  = join(publicDir, 'strategic-data-encrypted.json')
const BACKUP_FILE  = join(publicDir, 'strategic-data-unified.json.plaintext-backup')
const STUB_CONTENT = JSON.stringify({ encrypted: true, use: 'strategic-data-encrypted.json' }, null, 2)

const PBKDF2_ITERATIONS = 100_000
const SALT_BYTES        = 16
const IV_BYTES          = 12
const KEY_BITS          = 256
const KEY_BYTES         = KEY_BITS / 8

function toBase64(buf) {
  return Buffer.isBuffer(buf) ? buf.toString('base64') : Buffer.from(buf).toString('base64')
}

function encrypt(plaintext, password) {
  const salt = randomBytes(SALT_BYTES)
  const iv   = randomBytes(IV_BYTES)

  // PBKDF2 key derivation
  const key  = pbkdf2Sync(password, salt, PBKDF2_ITERATIONS, KEY_BYTES, 'sha256')

  // AES-256-GCM encryption
  const cipher = createCipheriv('aes-256-gcm', key, iv)
  const encrypted = Buffer.concat([
    cipher.update(plaintext, 'utf8'),
    cipher.final()
  ])
  const authTag = cipher.getAuthTag()          // 16-byte GCM auth tag

  // Concat ciphertext + authTag so the browser can split off the last 16 bytes
  const dataWithTag = Buffer.concat([encrypted, authTag])

  return {
    v:    1,
    salt: toBase64(salt),
    iv:   toBase64(iv),
    data: toBase64(dataWithTag)
  }
}

// ── Main ────────────────────────────────────────────────────────────────────

const password = process.argv[2] || process.env.DATA_PASSWORD

if (!password) {
  console.error('ERROR: No password provided.')
  console.error('Usage: node scripts/encrypt-data.mjs <password>')
  console.error('   or: DATA_PASSWORD=<password> node scripts/encrypt-data.mjs')
  process.exit(1)
}

console.log('Reading', INPUT_FILE)
const plaintext = readFileSync(INPUT_FILE, 'utf8')

console.log(`Encrypting ${plaintext.length} bytes with AES-256-GCM (PBKDF2 ${PBKDF2_ITERATIONS} iterations)…`)
const payload = encrypt(plaintext, password)

// 1. Write encrypted output
writeFileSync(OUTPUT_FILE, JSON.stringify(payload, null, 2), 'utf8')
console.log('Written:', OUTPUT_FILE, `(${JSON.stringify(payload, null, 2).length} bytes)`)

// 2. Write plaintext backup
writeFileSync(BACKUP_FILE, plaintext, 'utf8')
console.log('Written backup:', BACKUP_FILE)

// 3. Replace original with stub
writeFileSync(INPUT_FILE, STUB_CONTENT, 'utf8')
console.log('Replaced', INPUT_FILE, 'with stub')

console.log('\nDone. Fields in encrypted output:')
console.log('  v   :', payload.v)
console.log('  salt:', payload.salt.slice(0, 12) + '…  (base64, 16 bytes)')
console.log('  iv  :', payload.iv.slice(0, 12)   + '…  (base64, 12 bytes)')
console.log('  data:', payload.data.slice(0, 20)  + '…  (base64, ciphertext+authTag)')
