// 入力値変更時にエラーをクリア
$(document).on('input change', '.validate-input', function () {
  $(this).removeClass('is-invalid');
});