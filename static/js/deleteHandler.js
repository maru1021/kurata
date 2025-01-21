/**
 * 汎用的な削除処理関数
 * @param {string} url - 削除対象のエンドポイントURL
 * @param {DataTable} [options.dataTable] - 更新するデータテーブル
 */
export function handleDelete(url, dataTable) {
  $.ajax({
    url: url,
    type: 'DELETE',
    headers: { 'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val() },
    success: function (data) {
      if (data.success) {
        toastr.success(data.message || '削除が成功しました');
        dataTable.ajax.reload(null, false);
        $('#deleteConfirmationModal').modal('hide');
      } else {
        toastr.error(data.message || '削除に失敗しました');
      }
    },
    error: function (xhr, status, error) {
      toastr.error('エラーが発生しました。');
    },
  });
}
