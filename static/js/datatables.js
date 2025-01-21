function initializeDataTable(selector, url, columns) {
    return $(selector).DataTable({
        "ajax": {
            "url": url,
            "type": "GET",
            "dataSrc": "",
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
            "infoFiltered": "（全 _MAX_ 件から絞り込み）",
            "search": "検索:",
            "paginate": {
                "next": "次",
                "previous": "前"
            },
            "loadingRecords": "読み込み中...",
            "processing": "処理中...",
            "emptyTable": "テーブルにデータがありません。",
            "thousands": ","
        },
        "columns": columns,
        "rowId": "id",
    });
}
