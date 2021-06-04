using Newtonsoft.Json;
using System;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

namespace CryptoProjects
{
    class CryproParse
    {
       
        public static void Main(string[] args)
        {
            CheckLogs();
            SerializableAsync();
        }

        private static void CheckLogs()
        {
            string path = @$"Logs";
            DirectoryInfo dirInfo = new DirectoryInfo(path);

            if (!dirInfo.Exists)
            {
                dirInfo.Create();
            }
        }
        private static string GetNowDate()
        {
            return DateTime.Now.ToString("dd.MM.yyyy");
        }
        private static string GetNowTime()
        {
            return DateTime.Now.ToString("HH_mm_ss");
        }

        private static string getPathAndCreate(string CryptoName)
        {
            string nowDate = GetNowDate();
            string path = @$"Crypto\{CryptoName}";
            DirectoryInfo dirInfo = new DirectoryInfo(path);

            if (!dirInfo.Exists)
            {
                dirInfo.Create();
            }
            return path + @"\" + nowDate + ".json";
        }

        public static string FetchData(string url)
        {
            string String_jsonData;

            using (WebClient client = new WebClient())
            {
                Uri SourceUri = new Uri(url);

                String_jsonData = client.DownloadString(SourceUri);
            }
            return String_jsonData;
        }
        private static void SerializableAsync()
        {
            try
            {
                var url = GetUrl();
               
                Console.WriteLine($"url={url}");
                 var json = FetchData(url);
                    Console.WriteLine($"json={json}");
                    var info = JsonConvert.DeserializeObject<JsonInfo>(json);
                    Console.WriteLine($"info={info}");

                    var BTC = new CryptoItem
                        {
                            Date = DateTime.Now.ToString("G"),
                            USD = info.BTC.USD,
                            EUR = info.BTC.EUR
                        };
                    WriteCryptoInFiles(BTC, "BTC");
                    var ETH = new CryptoItem
                        {
                        Date = DateTime.Now.ToString("G"),
                            USD = info.ETH.USD,
                            EUR = info.ETH.EUR
                        };
                    WriteCryptoInFiles(ETH, "ETH");
                    var XLM = new CryptoItem
                    {
                        Date = DateTime.Now.ToString("G"),
                        USD = info.XLM.USD,
                        EUR = info.XLM.EUR
                    };
               
                    WriteCryptoInFiles(XLM, "XLM");
                    var BNB = new CryptoItem
                        {
                        Date = DateTime.Now.ToString("G"),
                            USD = info.BNB.USD,
                            EUR = info.BNB.EUR
                        };
                    WriteCryptoInFiles(BNB, "BNB");
                    var Doge = new CryptoItem
                        {
                        Date = DateTime.Now.ToString("G"),
                            USD = info.Doge.USD,
                            EUR = info.Doge.EUR
                        };
                    WriteCryptoInFiles(Doge, "Doge");
                    var LTC = new CryptoItem
                        {
                        Date = DateTime.Now.ToString("G"),
                            USD = info.LTC.USD,
                            EUR = info.LTC.EUR
                        };
                    WriteCryptoInFiles(LTC, "LTC");
                    var XRP = new CryptoItem
                        {
                        Date = DateTime.Now.ToString("G"),
                            USD = info.XRP.USD,
                            EUR = info.XRP.EUR
                        };
                    WriteCryptoInFiles(XRP, "XRP");
                    var BCH = new CryptoItem
                        {
                        Date = DateTime.Now.ToString("G"),
                            USD = info.BCH.USD,
                            EUR = info.BCH.EUR
                        };
                    WriteCryptoInFiles(BCH, "BCH");
                    var EOS = new CryptoItem
                        {
                        Date = DateTime.Now.ToString("G"),
                            USD = info.EOS.USD,
                            EUR = info.EOS.EUR
                        };
                    WriteCryptoInFiles(EOS, "EOS");
                   
                    var TRX = new CryptoItem
                        {
                        Date = DateTime.Now.ToString("G"),
                            USD = info.TRX.USD,
                            EUR = info.TRX.EUR
                        };
                    WriteCryptoInFiles(TRX, "TRX");
                    var DASH = new CryptoItem
                        {
                        Date = DateTime.Now.ToString("G"),
                            USD = info.DASH.USD,
                            EUR = info.DASH.EUR
                        };
                    WriteCryptoInFiles(DASH, "DASH");
                    var LINK = new CryptoItem
                        {
                        Date = DateTime.Now.ToString("G"),
                            USD = info.LINK.USD,
                            EUR = info.LINK.EUR
                        };
                    WriteCryptoInFiles(LINK, "LINK");
            }
            catch (Exception e)
            {
                ExceptionLogs(e);
            }
        }
        private static void WriteCryptoInFiles(CryptoItem infosForSerialize, string cryptoName)
        {
            try
            {
                var options = new JsonSerializerOptions
                {
                    WriteIndented = true
                };
                var jsonString = System.Text.Json.JsonSerializer.Serialize(infosForSerialize, options);

                var outputPath = getPathAndCreate(cryptoName);

                using (StreamWriter sw = new StreamWriter(outputPath, true, System.Text.Encoding.Default))
                {
                    sw.WriteLine(jsonString);
                }
            }
            catch (Exception e)
            {
                ExceptionLogs(e);
            }
            
        }
        private static void ExceptionLogs(Exception e)
        {
            var path = "Logs//" + GetNowDate() + ".txt";
            using (StreamWriter sw = new StreamWriter(path, true, System.Text.Encoding.Default))
            {
                sw.WriteLine($"{GetNowTime()}:{e.Message}");
            }
        }
        string FullUrl = $"https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,XRP,BNB,DOGE,LTC,BCH,EOS,XLM,TRX,DASH,LINK&tsyms=USD,EUR&api_key=1008c070e8a636f8ff756206ce6dd9895cda97fb90a877cccf7801c139da8419";
        private static string GetUrl ()
        {
            try
            {
                string cryptoName = "BTC,ETH,XRP,BNB,DOGE,LTC,BCH,EOS,XLM,TRX,DASH,LINK";
                string apiKey = "1008c070e8a636f8ff756206ce6dd9895cda97fb90a877cccf7801c139da8419";
                string valute = "USD,EUR";
                return "https://min-api.cryptocompare.com/data/pricemulti?fsyms=" + cryptoName + "&tsyms=" + valute + "&api_key=" + apiKey;
            }
            catch (Exception e)
            {
                ExceptionLogs(e);
                return null;
            }
         
        }
    }
}
