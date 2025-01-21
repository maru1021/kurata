/**
 * テーブル行の右クリックでコンテキストメニューを表示する汎用関数
 * @param {string} tableSelector - 対象のテーブルのセレクタ
 * @param {string} menuSelector - コンテキストメニューのセレクタ
 * @param {function} onRowSelect - 行が選択されたときのコールバック関数
 * @returns {object} - 選択された行データ
 */
export function initializeContextMenu(tableSelector) {
  let selectedRowData = null;

  $(`${tableSelector} tbody`).on('contextmenu', 'tr', function (e) {
    e.preventDefault();
    const table = $(tableSelector).DataTable();
    const row = table.row(this);
    selectedRowData = row.data();

    $('#contextMenu').css({
      display: 'block',
      top: e.pageY + 'px',
      left: e.pageX + 'px',
    });
  });

  $(document).on('click', () => $('#contextMenu').hide());

  return {
    getSelectedRowData: () => selectedRowData,
  };
}

export function showContextEdit(setupModal, selectedRowData, title, buttonText = '編集') {
  if (selectedRowData) {
    setupModal(title, buttonText, selectedRowData);
    $('#commonModal').modal('show');
  }
}

export function showContextDelete(deleteName) {
  $('#deleteName').text(deleteName);
  $('#deleteConfirmationModal').modal('show');
}
