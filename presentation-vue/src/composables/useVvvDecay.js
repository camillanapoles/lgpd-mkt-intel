// Composable: useVvvDecay
// Purpose: VVV decay temporal calculation per CLAUDE.md GOVERNANCE R1.
// Formula: vvv_decay = vvv × 1 / (1 + 0.30 × months_since_update)
// Returns reactive helpers + raw functions.

export function useVvvDecay(decayLambda = 0.30) {
  const monthsBetween = (updatedISO, now = Date.now()) => {
    if (!updatedISO) return 0
    const updated = new Date(updatedISO).getTime()
    return (now - updated) / (30.44 * 24 * 60 * 60 * 1000)
  }

  const computeDecay = (vvv, updatedISO) => {
    if (typeof vvv !== 'number') return 0
    if (!updatedISO) return vvv
    const months = monthsBetween(updatedISO)
    return vvv * (1 / (1 + decayLambda * months))
  }

  const decayLabel = (decayValue) => {
    if (decayValue >= 0.8) return 'Atual'
    if (decayValue >= 0.5) return 'Envelhecendo'
    if (decayValue >= 0.3) return 'Cautela — revalidar'
    return 'STALE — revalidacao necessaria'
  }

  return { computeDecay, monthsBetween, decayLabel, decayLambda }
}
