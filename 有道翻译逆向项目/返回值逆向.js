var CryptoJS = require('crypto-js')
var n = 'Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ytQNvu-WLU94qULZQ72aml6Jh8cIaWfLDqe22fTIyUU338TLmtutRx9thoVTDvyqjRe9c9k1kGoI1cHkCVEuYP-wpbIm0ROJO6-PveLLLs0UnHfdrEZ_xb-m7iyN6vLy1WBc_tnyKFL3cbR3NVNMuu3kLqFVl-iNZjHZHRUPZiABdcmSQwvC1ItEgcxe50pSO1onEZ6YworWuGIeVhJx1IL87ZO_kr-P2u30FTUiHlLrabyw5onmWOFK4xsjlVpuiN0oV__QC7FfhVr5C5BsxdXGjYBytECfksdak6OoZ0_3Rmuh8XKMrgnzEUfzD3sSLxk_grt1GLuRjC-vBdvectE4tUrBcBDbubFHEZwdG-Nde9PBUY4b5TFi6p4477UxIIA06TMt1lIjLrjYyomfV5QSm1WO2-I3VB78go32ELCpTVpE4DADAxkoATqAj4vOBo-Wpdni0Fbkh2DlIEaqUQNKyZext-RIY4G9Snmi8gx5e4H6iOLe5Ynk7SZ1qQ2YbsCcKrF2iZIULVWKFDeigMGTLaa4_JkVTPQa1YeTm7OJThbPV-_CjG8lZNjs7xos6xAjdLPMfZeJ2QlNspNt7iAOhyh6XvLmq5yjovXyCOwb52iGcCDrTr-8NpYB2pITmfVCKa5DtFaFndCiT0B7phq0t7-MUj5cEcVlvVZGVdUK2CfCR3mtS50o44CFm0qFpNDuFGodrbSv5aWAJRodkFObw-DA9R7RxhwxT0oxVdJOcEhlZHZmMO8sJMZDXj2gCq9gbkmyEQ0SAFh_0Mm9BB8Oo_uFHUcM72xAbovUqxyMd97fRyp66LDtR9BwUX0REruT4mC2un6LPoJhGmo5ZhIaqIy8ACNqF6YQ_TsRHxVKoCf3I1pukVFuOPIJZj_elM-ao4LqtFWL6Yfoy4ujx0I901fFPdVWyWvipw_lPbahI2LA4Uect1GkjH_V6Ok2xFVMyr5-Kimc2dk4I9Pz3LDc4pgcSSMHix7He7T0t4dovyCfUzV-8Q3lsjYmIc5pXreW0xSZhoX-P7a0X7sRWlMQCxfKyBaPc_urpt9Nj-kK2cXoM8orh2hhfQLxrQs9WGQ971qvc4X5zsUypARDi2n2umlqIuE7odQWCfS9LZfIhmui4GJYk-GF-ewvpGpp3nWfskpJU7XvNhZTP-N3eKjwk2aY80WZG8TwVlWxz7pqTd0ahvJowMExOxEkDEJ72Y='
// function aes_decode(content) {
//   return CrytoJS.AES.decrypt(content)
// }
var my_md5 = function(mes) {
  return CryptoJS.MD5(mes).toString() //.toUpperCase()
}
var alloc = function(t, e, n) {
  return l(null, t, e, n)
}
function m(e) {
  return my_md5(e)
  // return c.a.createHash("md5").update(e).digest()
}
function encryptAes(data, key_value, iv_value) {
  console.log(m(key_value))
  var key = alloc(16, m(key_value))
  var iv = alloc(16, m(iv_value))
  console.log(key)
  // var key  = CryptoJS.enc.Latin1.parse(key_value);
  // var iv   = CryptoJS.enc.Latin1.parse(iv_value);
  return CryptoJS.AES.decrypt(data, key, {iv:iv,mode:CryptoJS.mode.CBC,padding:CryptoJS.pad.ZeroPadding}).toString();
}

// function h(t, e, n) {
//   if (!h.TYPED_ARRAY_SUPPORT && !(this instanceof h))
//       return new h(t,e,n);
//   if ("number" === typeof t) {
//       if ("string" === typeof e)
//           throw new Error("If encoding is specified then the first argument must be a string");
//       return d(this, t)
//   }
//   return f(this, t, e, n)
// }
// h.alloc = function(t, e, n) {
//   return l(null, t, e, n)
// }
// function m(e) {
//   return c.a.createHash("md5").update(e).digest()
// }
// A = (t,o,n)=>{
//   if (!t)
//       return null;
//   const a = h.alloc(16, m(o))
//     , r = h.alloc(16, m(n))
//     , i = c.a.createDecipheriv("aes-128-cbc", a, r);
//   let s = i.update(t, "base64", "utf-8");
//   return s += i.final("utf-8"),
//   s
// }
var decodeKey = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
var decodeIv = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'
var result = encryptAes(n, decodeKey, decodeIv)
console.log(result)
