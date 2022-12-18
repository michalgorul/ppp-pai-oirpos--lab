import React from 'react';

const ChatMessage = ({ message }) => {
  const { message_from_user_id, message_text } = message;
  return (
    <div>
      Od: {message_from_user_id} - „{message_text}”
    </div>
  );
};

export default ChatMessage;
