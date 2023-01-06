import React, { useEffect, useState, useContext, useRef } from 'react';

import { useParams } from 'react-router-dom';

import { AuthContext } from '../AuthContextProvider';

import apiClient from '../apiClient';

import ChatMessage from '../components/ChatMessage';

const Chat = () => {
  const params = useParams(); // Pobierz parametry ścieżki url
  const messageToUserId = params.id;
  const [messages, setMessages] = useState([]);

  const { isLoggedIn } = useContext(AuthContext);

  const [messageText, setMessageText] = useState('');

  useEffect(() => {
    apiClient.getMessages(params.id).then(r => setMessages(r));
  }, [params, params.id]);

  // TODO:WEBSOCKET Zdefinuj WebSocket tak aby przy odebraniu nowej wiadomości, lista
  // wiadomości została aktualizowana o nową wiadomość

  const sendMessageWebSocket = message => {
    if (ws.current) {
      ws.current.send(message);
    }
  };

  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocket('ws://localhost:8081', [], {
      Cookie: document.cookie,
    });
    ws.current.onopen = () => {
      console.log('ws onopen');
    };
    ws.current.onclose = () => console.log('ws onclose');
    ws.current.onmessage = e => {
      console.log(e.data);
      // TODO: Przechwyć wiadomość tutaj.
      setMessages([...messages, e.data])
    };
    const currentWS = ws.current;
    return () => currentWS.close();
  }, []);

  if (!isLoggedIn) {
    return <p>Zaloguj się aby wyświetlić chat z tym użytkownikiem</p>;
  }

  return (
    <>
      <div>
        <h1>Chat ID = {messageToUserId}</h1>
        <div style={{ backgroundColor: '#453e3d' }}>
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
              is='textarea'
              onChange={e => setMessageText(e.target.value)}
            />
          </div>
          <div>
            <button
              type='submit'
              onClick={e => {
                e.preventDefault();
                sendMessageWebSocket(messageText);
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
