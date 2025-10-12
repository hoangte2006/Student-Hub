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

