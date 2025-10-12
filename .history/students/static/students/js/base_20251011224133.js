document.addEventListener('DOMContentLoaded', function () {
  const bubble = document.getElementById('aiBubble');
  if (bubble) {
    bubble.addEventListener('click', () => {
      alert('👋 Chào Te! Em cần anh giúp gì không?');
    });
  } else {
    console.warn('Không tìm thấy phần tử #aiBubble');
  }
});

document.addEventListener('DOMContentLoaded', function () {
  const input = document.getElementById('aiInput');
  const messages = document.getElementById('aiMessages');

  const fakeReplies = [
    "Anh đang xử lý câu hỏi của em...",
    "Hãy thử chọn lớp khác để xem biểu đồ nhé!",
    "Em cần anh giúp gì về học lực?",
    "Biểu đồ đã được cập nhật rồi đó!",
    "Dữ liệu lớp này hơi ít, em thử lớp khác nha!"
  ];

  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
      const text = input.value.trim();
      if (!text) return;

      messages.innerHTML += `<div><b>Em:</b> ${text}</div>`;

      const reply = fakeReplies[Math.floor(Math.random() * fakeReplies.length)];
      setTimeout(() => {
        messages.innerHTML += `<div><b>AI:</b> ${reply}</div>`;
        messages.scrollTop = messages.scrollHeight;
      }, 500);

      input.value = '';
    }
  });
});
