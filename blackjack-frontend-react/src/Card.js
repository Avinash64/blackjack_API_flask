import React from 'react'
import "./Card.css"

const display_suit = (suit) => {
  if (suit === 'H'){
    return '♥'
  }
  if (suit === 'S'){
    return '♠'
  }
  if (suit === 'D'){
    return '♦'
  }
  if (suit === 'C'){
    return '♣'
  }
}

function Card(props) {
  var [num, suit] = props.card.split('_') 
  return (
    <div className='playingCard card' style={{color: "HD".includes(suit) ? "red": "black" }}>{num}{display_suit(suit)}</div>
  )
}

export default Card