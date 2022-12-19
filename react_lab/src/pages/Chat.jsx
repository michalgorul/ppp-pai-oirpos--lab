import React, { useEffect, useState, useContext, useRef } from 'react';

import { useParams } from 'react-router-dom';

import { AuthContext } from '../AuthContextProvider';

import apiClient from '../apiClient';

import ChatMessage from '../components/ChatMessage';

const Chat = () => {
  const params = useParams(); // Pobierz parametry ścieżki url
  const messageToUserId = params.id;
  const [messages, setMessages] = useState([]);

  const { isLoggedIn, setIsLoggedIn } = useContext(AuthContext);

  const [messageText, setMessageText] = useState('');

  // TODO: Przy pierwszym załadowaniu komponenetu (użyj useEffect) pobierz listę
  // wszystkich wiadomości za pomocą funkcji getMessages z pliku apiClient.jsx.
  // Zapisz/Ustaw otrzymane wiadomości w zmiennej stanu "messages"
  useEffect(() => {
    apiClient.getMessages(params.id).then(r => setMessages(r));
  }, [params, params.id]);

  // TODO:WEBSOCKET Zdefinuj WebSocket tak aby przy odebraniu nowej wiadomości, lista
  // wiadomości została aktualizowana o nową wiadomość

  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocket('ws://localhost:8080');
    ws.current.onopen = () => console.log('ws onopen');
    ws.current.onclose = () => console.log('ws onclose');
    console.log(ws.current);
    ws.current.onmessage = e => {
      console.log(e);
      // TODO: Przechwyć wiadomość tutaj.
    };
    // const currentWS = ws.current;
    // return () => currentWS.close();
  }, []);

  if (!isLoggedIn) {
    return <p>Zaloguj się aby wyświetlić chat z tym użytkownikiem</p>;
  }

  return (
    <>
      <div>
        <h1>Chat ID = {messageToUserId}</h1>
        <div style={{ backgroundColor: 'lightgrey', maxHeight: '600px' }}>
          {messages.length === 0 || !messages.length ? (
            <p>Brak wiadomości</p>
          ) : (
            <></>
          )}
          {messages.length &&
            messages.map((message, idx) => {
              return (
                <ChatMessage key={`chat-message-${idx}`} message={message} />
              );
            })}
        </div>
      </div>
      <div>
        <form>
          <div>
            <label>Wiadomość</label>
            <input
              type='text'
              as='textarea'
              onChange={e => setMessageText(e.target.value)}
            />
          </div>
          <div>
            <button
              type='submit'
              onClick={e => {
                e.preventDefault();
                apiClient
                  .sendMessages(messageText, messageToUserId)
                  .then(r => console.log(r));
              }}
            >
              Wyślij wiadomość
            </button>
          </div>
        </form>
      </div>
    </>
  );
};

export default Chat;
