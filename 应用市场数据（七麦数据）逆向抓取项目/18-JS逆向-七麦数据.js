/*
a = 'MDUwMDA=@#/indexV2/getIndexRank@#14193964720@#3'
d = 'xyz517cda96abcd'
i[jt](i[qt](a, d))
== > 
param = i[qt](a, d)
analysis = i[jt](param)
*/

// var a = 'MDUwMDA=@#/indexV2/getIndexRank@#14193964720@#3'
// var d = 'xyz517cda96abcd'

// 破解a参数和d参数
// a参数

function get_ad(genre) {
  var t = {
    baseURL: "https://api.qimai.cn",
    params: {setting: 0, genre: genre},
    url: "/indexV2/getIndexRank"
  }
  var a = []
  a['push'](t.params['setting'])
  a['push'](t.params['genre'])
  a = a['sort']()['join']('')
  a = v(a)
  var r = +new Date() - (1064 || 0) - 1661224081041
  a = (a += '@#' + t.url['replace'](t.baseURL, '')) + ('@#' + r) + ('@#' + 3)
  // d参数
  function y(n, t, e) {
    for (var r = void 0 === e ? 2166136261 : e, a = 0, i = n['length']; a < i; a++)
        r = (r ^= n['charCodeAt'](a)) + ((r << 1) + (r << 4) + (r << 7) + (r << 8) + (r << 24));
    return t ? ('xyz' + (r >>> 0)['toString'](16) + 'abcd')['substr'](-16) : r >>> 0
  }
  var d = y('qimai@2022&Technology', 1)
  return [a, d]
}

// analysis 参数逆向破解

function o(n) {
  t = '',
  ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']['forEach'](function(n) {
      t += unescape('%u00' + n)
  });
  var t, e = t;
  return String[e](n)
}

function h(n, t) {
  t = t || u();
  for (var e = (n = n['split'](''))['length'], r = t['length'], a = 'charCodeAt', i = 0; i < e; i++)
      n[i] = o(n[i][a](0) ^ t[(i + 10) % r][a](0));
  return n['join']('')
}

function v(t) {
  t = encodeURIComponent(t)['replace'](/%([0-9A-F]{2})/g, function(n, t) {
      return o('0x' + t)
  });
  try {
      return btoa(t)
  } catch (n) {
      return Buffer.from(t)['toString']('base64')
  }
}

// analysis参数破解完成
function get_analysis(genre){
  var ad = get_ad(genre)
  a = ad[0]; d = ad[1]
  middle_param = h(a, d)
  analysis = v(middle_param)
  return analysis
}
console.log(get_analysis('5000'))
