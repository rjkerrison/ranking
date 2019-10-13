import React from 'react'
import { BrowserRouter as Router, Route } from 'react-router-dom'

import Songs from './songs'
import Scores from './scores'
import Contest from './contest'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      songs: [],
      scores: []
    }
  }

  componentDidMount() {
    fetch('/songs')
      .then(res => res.json())
      .then((data) => {
        this.setState({ songs: data })
      })
      .catch(console.log)

    fetch('/songs/scores')
      .then(res => res.json())
      .then((data) => {
        this.setState({ scores: data })
      })
      .catch(console.log)
  }

  render() {
    return (
      <Router>
        <Route exact path='/'>
          <Songs songs={this.state.songs} />
        </Route>
        <Route path='/scores'>
          <Scores scores={this.state.scores} />
        </Route>
        <Route path='/contest/:id' render={({match}) => <Contest {...match} />} />
      </Router>
    )
  }
}

export default App
