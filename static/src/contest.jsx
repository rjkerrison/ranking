import React from 'react'
import { useParams } from 'react-router-dom'

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
      <ul>
        {this.state.contestants.map(c => <li key={c}>{c}</li>)}
      </ul>
    )
  }
}

export default Contest
