import { useState } from 'react'
import './App.css'

export default function App() {
  const [age, setAge] = useState('45')
  const [smoking, setSmoking] = useState('never')
  const [familyHistory, setFamilyHistory] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState('')

  async function calculate(event) {
    event.preventDefault()
    setError('')
    setResult(null)

    try {
      const response = await fetch('/api/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          age: Number(age),
          smoking,
          family_history: familyHistory,
        }),
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.error || 'Calculation failed')
      }

      setResult(data)
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <main className="container">
      <h1>Cancer Risk Calculator</h1>
      <p>Educational Full Stack Portfolio Project</p>

      <section className="card">
        <h2>Example inputs</h2>

        <form onSubmit={calculate}>
          <label htmlFor="age">Age</label>
          <input
            id="age"
            type="number"
            min="18"
            max="100"
            value={age}
            onChange={(e) => setAge(e.target.value)}
            required
          />

          <label htmlFor="smoking">Smoking status</label>
          <select
            id="smoking"
            value={smoking}
            onChange={(e) => setSmoking(e.target.value)}
          >
            <option value="never">Never</option>
            <option value="former">Former</option>
            <option value="current">Current</option>
          </select>

          <label className="checkbox">
            <input
              type="checkbox"
              checked={familyHistory}
              onChange={(e) => setFamilyHistory(e.target.checked)}
            />
            Example family history
          </label>

          <button type="submit">Calculate demo score</button>
        </form>

        {error && <p role="alert" className="error">{error}</p>}
      </section>

      {result && (
        <section className="card result">
          <h2>Educational result</h2>
          <div className="score">
            {result.demo_score} / {result.max_score}
          </div>
          <p>{result.disclaimer}</p>
        </section>
      )}

      <footer>
        Fictional scoring rules only. Not a medical risk estimate
        or medical advice.
      </footer>
    </main>
  )
}
