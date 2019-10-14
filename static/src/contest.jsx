import React from 'react'
import { useParams } from 'react-router-dom'

import Button from '@material-ui/core/Button'

class Contest extends React.Component {
  constructor(props) {
    super(props)
  }

  render() {
    return (
      <div>
        {this.props.contestants.map(c =>
          <Contestant
            key={`contestant_${c}`}
            name={c}
            click={this.props.click.bind(this)}
            />)}
      </div>
    )
  }
}

class Contestant extends React.Component {
  click() {
    this.props.click(this.props.name)
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
