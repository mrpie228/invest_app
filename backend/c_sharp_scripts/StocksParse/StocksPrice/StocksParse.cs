using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Net;

namespace StocksPrice
{
    class Stocks
    {
        static void Main()
        {
            CheckLogs();
            Serializable();
        }
        
        private static void Serializable()
        {
            Stopwatch stopwatch = new Stopwatch();

            try
            {
                stopwatch.Start();
             
                var url = GetUrl();

                Console.WriteLine($"url={url}");
                var json = FetchData(url);
                var info = JsonConvert.DeserializeObject<List<ParseProperty>>(json);

                foreach (var item in info)
                {
                    Console.WriteLine($"price {item.Price}, Name {item.Name}, Symbol {item.Symbol}, Exchange {item.Exchange}");
                }

                stopwatch.Stop();
                TimeSpan timeSpan = stopwatch.Elapsed;

                Console.WriteLine("Время работы скрипта: {0}h {1}m {2}s {3}ms", timeSpan.Hours, timeSpan.Minutes, timeSpan.Seconds, timeSpan.Milliseconds);

            }
            catch (Exception e)
            {
                ExceptionLogs(e);
            }
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
        private static string GetUrl()
        {
            try
            {
                string category = "stock";
                string apiKey = "6fabf6f3f1bd58c44caaceb6e148c96a";
                return "https://financialmodelingprep.com/api/v3/" + category + "/list?apikey=" + apiKey;
            }
            catch (Exception e)
            {
                ExceptionLogs(e);
                return null;
            }
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
        private static string GetNowDate()
        {
            return DateTime.Now.ToString("dd.MM.yyyy");
        }
        private static string GetNowTime()
        {
            return DateTime.Now.ToString("HH_mm_ss");
        }

        private static void ExceptionLogs(Exception e)
        {
            var path = "Logs//" + GetNowDate() + ".txt";
            using (StreamWriter sw = new StreamWriter(path, true, System.Text.Encoding.Default))
            {
                sw.WriteLine($"{GetNowTime()}:{e.Message}");
            }
        }
    }
}
