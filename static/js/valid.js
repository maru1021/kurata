/**
 * フィールドのバリデーションを行う汎用関数
 * @param {Array} rules - バリデーションルールの配列
 * @returns {boolean} - 全てのフィールドが有効かどうか
 */
export function validateFields(rules) {
  let isValid = true; // 全体のバリデーションフラグ

  rules.forEach(({ field, feedbackSelector, errorMessage, type }) => {
    const value = $(field).val();
    // 空白時のバリデーション
    if (!value || value.trim() === '') {
      $(field).addClass('is-invalid');
      $(feedbackSelector).text(errorMessage);
      isValid = false;
    } else if(type === 'date'){
      // 日付のバリデーション
      const dateRegex = /^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$/;
      if(!dateRegex.test(value)){
        console.log(value);
        $(field).addClass('is-invalid');
        $(feedbackSelector).text(errorMessage);
        isValid = false;
      }
    } else {
      $(feedbackSelector).text('');
    }
  });

  return isValid; // 最終的なバリデーション結果を返す
}
