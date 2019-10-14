import React from 'react'

const Scores = ({ scores }) => {
  console.log(scores)
  let keys = Object.keys(scores)
  keys.sort((a, b) => scores[b] - scores[a])

  return (
    <div>
      <h1>Song Scores</h1>
      {keys.map((song) => (
        <h2 key={song}>{song}: {scores[song]}</h2>
      ))}
    </div>
  )
}

export default Scores
