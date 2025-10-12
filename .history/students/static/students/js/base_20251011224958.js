document.addEventListener('DOMContentLoaded', function () {
  const input = document.getElementById('aiInput');
  const sendBtn = document.getElementById('aiSend');
  const messages = document.getElementById('aiMessages');
  const closeBtn = document.getElementById('aiClose');
  const popup = document.getElementById('aiPopup');
  const icon = document.getElementById('aiIcon');

  const fakeReplies = [
    "Anh đang xử lý câu hỏi của em...",
    "Hãy thử chọn lớp khác để xem biểu đồ nhé!",
    "Em cần anh giúp gì về học lực?",
    "Biểu đồ đã được cập nhật rồi đó!",
    "Dữ liệu lớp này hơi ít, em thử lớp khác nha!"
  ];

  // Load lịch sử chat từ localStorage
  const history = JSON.parse(localStorage.getItem('aiChatHistory') || '[]');
  history.forEach(msg => {
    messages.innerHTML += `<div><b>${msg.sender}:</b> ${msg.text}</div>`;
  });

  function sendMessage() {
    const text = input.value.trim();
    if (!text) return;

    messages.innerHTML += `<div><b>Em:</b> ${text}</div>`;
    saveToHistory('Em', text);

    const reply = fakeReplies[Math.floor(Math.random() * fakeReplies.length)];
    setTimeout(() => {
      messages.innerHTML += `<div><b>AI:</b> ${reply}</div>`;
      saveToHistory('AI', reply);
      messages.scrollTop = messages.scrollHeight;
    }, 500);

    input.value = '';
  }

  function saveToHistory(sender, text) {
    const updated = JSON.parse(localStorage.getItem('aiChatHistory') || '[]');
    updated.push({ sender, text });
    localStorage.setItem('aiChatHistory', JSON.stringify(updated));
  }
// nhấn Enter để gửi
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
      sendMessage();
    }
  });
// nhấn nút để gửi
  sendBtn.addEventListener('click', sendMessage);
  closeBtn.addEventListener('click', () => popup.style.display = 'none');
  icon.addEventListener('click', () => popup.style.display = 'block');
});
