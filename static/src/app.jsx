import React from 'react'
import { BrowserRouter as Router, Route } from 'react-router-dom'

import Songs from './songs'
import Scores from './scores'
import ContestPicker from './contestPicker'

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
      <div>
        <Scores scores={this.state.scores} />
        <Router>
          <Route path='/contest'>
            <ContestPicker />
          </Route>
        </Router>
      </div>
    )
  }
}

export default App
