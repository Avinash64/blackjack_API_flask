import React, { useState } from 'react';
import './App.css';
import Card from './Card';

const value = (hand) => {
  var total = 0
  for (var i = 0; i < hand.length; i++) {
    var card = hand[i];
    card = hand[i].split("_")[0]
    if ("JQK".includes(card)) {
      total += 10
    }
    else if (card === "A") {
      if (total >= 11) {
        total += 1
      }
      else {
        total += 11
      }
    }
    else {

      total += parseInt(card)
    }
  }
  return total
}

const result = {
  0: "Lose",
  1: "Win",
  2: "Tie"
}

function App() {
  const [gameId, setgameId] = useState()

  const [game, setGame] = useState()

  const createGame = () => {
    const options = { method: 'POST' };

    fetch('http://localhost:5000/create_game', options)
      .then(response => response.json())
      .then(response => { console.log(response); setgameId(response.gameId); setGame(response.game) })
      .catch(err => console.error(err));
  }


  const play = (game_id, action) => {
    const options = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: `{"game_id":${game_id},"action":${action}}`
    };

    fetch('http://localhost:5000/play', options)
      .then(response => response.json())
      .then(response => setGame(response))
      .catch(err => console.error(err));
  }

  return (
    <div className="App">
      <nav className="navbar navbar-dark bg-dark">
        <span className="navbar-brand mb-0 h1">BlackJack</span>

        <div className="nav-item">Game Id: {gameId ? gameId : "None"}</div>

      </nav>

      <div>Dealer: {game ? game.gameOver ? game.dealerHand.join(' ') : `${game.dealerHand[0]} ${"? ".repeat(game.dealerHand.length - 1)}` : 0}</div>

      <div>Player: {game ? value(game.playerHand) : 0}</div>

      <div>Player: {game ? 
      game.playerHand.map((card, index) => {
        return <Card key={index} card={card}></Card>
      })
      
      : 0}</div>


      <div>{game ? game.gameOver ? result[game.result] : '' : ''}</div>
      <div>

      <button className="btn btn-primary w-50" onClick={() => createGame()}>Create Game</button>
      <button className="btn btn-danger w-25" onClick={() => play(gameId, 1)} disabled={game ? game.gameOver ? true : false : true} >Hit</button>
      <button className="btn btn-info w-25" onClick={() => play(gameId, 2)} disabled={game ? game.gameOver ? true : false : true} >Stand</button>
      </div>

    </div>
  );
}

export default App;
