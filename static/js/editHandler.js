/**
 * 汎用的な削除処理関数
 * @param {string} url - 削除対象のエンドポイントURL
 * @param {method} string - ajax送信時のメソッド
 * @param {DataTable} [options.dataTable] - 更新するデータテーブル
 */
export function handleEdit(url, method, senddata, dataTable) {
  $.ajax({
    url: url,
    type: method,
    data: senddata,
    success: function (data) {
        if (data.success) {
            toastr.success(data.message);
            $('#commonModal').modal('hide');
            dataTable.ajax.reload(null, false);
        } else if(!data.error_field) {
            toastr.error(data.message);
        }else {
            $(`.invalid-feedback[for=${data.error_field}]`).text(data.message);
            $(`#${data.error_field}`).addClass('is-invalid');
        }
    },
    error: function () {
        toastr.error("エラーが発生しました。");
    }
  });
}
