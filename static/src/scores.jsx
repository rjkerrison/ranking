import React from 'react'

const Scores = ({ scores }) => {
  console.log(scores)

  return (
    <div>
      <h1>Song Scores</h1>
      {Object.keys(scores).map((song) => (
        <h2 key={song}>{song}: {scores[song]}</h2>
      ))}
    </div>
  )
}

export default Scores
