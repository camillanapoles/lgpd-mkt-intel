/**
 * crypto.ts — SubtleCrypto-based AES-GCM decryption for NeoGov Strategic Intelligence.
 * Populated by the encryption agent. This stub satisfies TypeScript during parallel builds.
 */

export interface EncryptedPayload {
  v: number
  salt: string
  iv: string
  data: string
}

/** Derive AES-GCM key from password + salt using PBKDF2 */
async function deriveKey(password: string, salt: Uint8Array<ArrayBuffer>): Promise<CryptoKey> {
  const enc = new TextEncoder()
  const keyMaterial = await crypto.subtle.importKey(
    'raw',
    enc.encode(password),
    'PBKDF2',
    false,
    ['deriveKey'],
  )
  return crypto.subtle.deriveKey(
    { name: 'PBKDF2', salt, iterations: 100_000, hash: 'SHA-256' },
    keyMaterial,
    { name: 'AES-GCM', length: 256 },
    false,
    ['decrypt'],
  )
}

/** Decode base64 string to a Uint8Array backed by a plain ArrayBuffer */
function b64ToBytes(b64: string): Uint8Array<ArrayBuffer> {
  const raw = atob(b64)
  const buf = new ArrayBuffer(raw.length)
  const view = new Uint8Array(buf)
  for (let i = 0; i < raw.length; i++) {
    view[i] = raw.charCodeAt(i)
  }
  return view
}

/**
 * Decrypt an EncryptedPayload with the given password.
 * Throws if the password is wrong or the payload is corrupt.
 */
export async function decryptPayload(
  payload: EncryptedPayload,
  password: string,
): Promise<unknown> {
  const salt = b64ToBytes(payload.salt)
  const iv = b64ToBytes(payload.iv)
  const ciphertext = b64ToBytes(payload.data)

  const key = await deriveKey(password, salt)

  const plaintext = await crypto.subtle.decrypt(
    { name: 'AES-GCM', iv },
    key,
    ciphertext,
  )

  return JSON.parse(new TextDecoder().decode(plaintext))
}

/**
 * Returns true if password successfully decrypts the payload, false otherwise.
 * Never throws.
 */
export async function testPassword(
  payload: EncryptedPayload,
  password: string,
): Promise<boolean> {
  try {
    await decryptPayload(payload, password)
    return true
  } catch {
    return false
  }
}
