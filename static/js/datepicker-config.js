// Datepickerの日本語ロケール設定
function setJapaneseDatepickerDefaults() {
  $.datepicker.regional['ja'] = {
      closeText: "閉じる",
      prevText: "",
      nextText: "",
      currentText: "今日",
      monthNames: ["1月", "2月", "3月", "4月", "5月", "6月",
          "7月", "8月", "9月", "10月", "11月", "12月"],
      monthNamesShort: ["1月", "2月", "3月", "4月", "5月", "6月",
          "7月", "8月", "9月", "10月", "11月", "12月"],
      dayNames: ["日曜日", "月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日"],
      dayNamesShort: ["日", "月", "火", "水", "木", "金", "土"],
      dayNamesMin: ["日", "月", "火", "水", "木", "金", "土"],
      weekHeader: "週",
      dateFormat: "yy-mm-dd",
      firstDay: 0,
      isRTL: false,
      showMonthAfterYear: true,
      yearSuffix: "年"
  };
  $.datepicker.setDefaults($.datepicker.regional['ja']);
}

// Datepickerの初期化関数
export function initializeDatepicker(selector) {
  setJapaneseDatepickerDefaults();
  const today = new Date();
  if (today.getHours() < 8) {
    today.setDate(today.getDate() - 1); // 8時以前の場合は前日
  }
  const formattedToday = today.toISOString().split("T")[0];

  $(selector).datepicker({
      changeMonth: true,
      changeYear: true,
      showButtonPanel: true,
      dateFormat: "yy-mm-dd",
      defaultDate: today,
      beforeShow: function (input, inst) {
          setTimeout(() => {
              inst.dpDiv.css({
                  background: "#f7f7f9",
                  border: "1px solid #ddd",
                  borderRadius: "10px",
                  padding: "10px"
              });
          }, 1);
      }
  }).val(formattedToday);
}
