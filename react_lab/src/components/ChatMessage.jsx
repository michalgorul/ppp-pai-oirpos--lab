import React from 'react';

const ChatMessage = ({ message }) => {
  const { messageFromUserId, messageText } = message;
  return (
    <div>
      Od: {messageFromUserId} - „{messageText}”
    </div>
  );
};

export default ChatMessage;
