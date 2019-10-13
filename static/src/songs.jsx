import React from 'react'

const Songs = ({ songs }) => {
  return (
    <div>
      <h1>Songs List</h1>
      {songs.map((song) => (
        <h2>{song}</h2>
      ))}
    </div>
  )
}

export default Songs
