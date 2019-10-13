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
        {this.state.contestants.map(c => <Button variant='contained' key={c}>{c}</Button>)}
      </div>
    )
  }
}

export default Contest
