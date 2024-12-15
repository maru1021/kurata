/**
 * 汎用的な DataTables 初期化関数
 * @param {string} selector - DataTables を初期化するテーブルのセレクタ
 * @param {string} url - Ajax でデータを取得するエンドポイントの URL
 * @param {Array} columns - DataTables に表示する列の設定
 * @returns {DataTable} - 初期化された DataTables オブジェクト
 */
function initializeDataTable(selector, url, columns) {
  return $(selector).DataTable({
      "ajax": {
          "url": url,
          "type": "GET",
          "dataSrc": "" // サーバーから返されるデータの形式に合わせて変更
      },
      "paging": true,
      "searching": true,
      "ordering": true,
      "info": true,
      "language": {
          "lengthMenu": "_MENU_ 件表示",
          "zeroRecords": "データが見つかりません。",
          "info": "全 _TOTAL_ 件中 _START_ 件から _END_ 件を表示",
          "infoEmpty": "データがありません。",
          "search": "検索:",
          "paginate": {
              "next": "次",
              "previous": "前"
          }
      },
      "columns": columns
  });
}
