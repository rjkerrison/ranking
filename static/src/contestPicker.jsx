import React from 'react'
import Contest from './contest'

class ContestPicker extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      contests: [],
      currentContest: {
        contestants: [],
        id: null
      }
    }
  }

  componentDidMount() {
    fetch('/songs/contests')
      .then(res => res.json())
      .then((data) => {
        this.setState({
          contests: data,
          currentContest: randomChoice(data)
        })
      })
      .catch(console.log)
  }

  click(choice) {
    console.log(this.state)
    let url = `/songs/contests/${this.state.currentContest._id}`

    fetch(url, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        winner: choice
      })
    })
    .then(() => {
      this.setState({
        currentContest: randomChoice(this.state.contests)
      })
    })
  }

  render() {
    return (
      <Contest {...this.state.currentContest} click={this.click.bind(this)} />
    )
  }
}

const randomChoice = (array) => array[Math.floor(array.length * Math.random())]

export default ContestPicker
