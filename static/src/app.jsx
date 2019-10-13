import React from 'react'

import Songs from './songs'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      songs: []
    }
  }

  componentDidMount() {
    fetch('/songs')
      .then(res => res.json())
      .then((data) => {
        this.setState({ songs: data })
      })
      .catch(console.log)
  }

  render() {
    return <Songs songs={this.state.songs} />
  }
}

export default App
