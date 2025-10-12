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
  input.addEventListener('keydown', async (e) => {
    if (e.key === 'Enter') {
      const text = e.target.value.trim();
      if (!text) return;

      const messages = document.getElementById('aiMessages');
      messages.innerHTML += `<div><b>Em:</b> ${text}</div>`;

      // Gọi API giả lập
      const reply = "Anh đang xử lý câu hỏi của em...";
      messages.innerHTML += `<div><b>AI:</b> ${reply}</div>`;
      e.target.value = '';
    }
  });
});
