function initializeDataTable(selector) {
  $(selector).DataTable({
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
      }
  });
}
