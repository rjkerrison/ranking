import React from 'react'
import { useParams } from 'react-router-dom'

import Button from '@material-ui/core/Button'

class Contest extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      contestants: []
    }
  }

  componentDidMount() {
    let url = `/songs/contests/${this.props.params.id}`

    fetch(url)
      .then(res => res.json())
      .then((data) => {
        this.setState(data[0])
      })
      .catch(console.log)
  }

  render() {
    return (
      <div>
        {this.state.contestants.map(c => <Contestant key={`contestant_${c}`} id={this.props.params.id} name={c}/>)}
      </div>
    )
  }
}

class Contestant extends React.Component {
  click() {
    let url = `/songs/contests/${this.props.id}`

    fetch(url, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        winner: this.props.name
      })
    })
  }

  render() {
    return (
      <Button
        key={`button_${this.props.name}`}
        onClick={this.click.bind(this)}
        variant='contained'>
        {this.props.name}
      </Button>
    )
  }
}

export default Contest
