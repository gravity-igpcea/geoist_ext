using System;
using System.IO;
using System.Text;
using Newtonsoft.Json.Linq;

namespace NodePlugin
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length < 1)
            {
                Console.WriteLine("参数据文件不存在");
                return;
            }
            var jsonFile = args[0];

            var txt = File.ReadAllText(jsonFile, Encoding.UTF8);
            var data = JObject.Parse(txt);

            Console.WriteLine("----NodeTest.exe by bushyao----");

            // 前节点的输出文件名
            Console.WriteLine("magdata:" + data["magdata"]);
            Console.WriteLine("magdata2:" + data["magdata2"]);
            Console.WriteLine("OutputPath:" + data["OutputPath"]);

            Console.WriteLine("中文永远是个坑");
            Console.WriteLine("title:" + data["pars"]["title"]);
            Console.WriteLine("desc:" + data["pars"]["desc"]);

            //输出一个文件
            Console.WriteLine("D:\\MyProgram\\RDMS\\PPTAnalysis\\binX\\Plugin\\test\\tmpData\\asia150dpi.png");

            //输出数据表格文件
            Console.WriteLine("D:\\MyProgram\\RDMS\\PPTAnalysis\\binX\\Plugin\\test\\tmpData\\tmp5DAC.csv");

            //输出网页
            Console.WriteLine("http://www.baidu.com");   //输出网络地址 
        }
    }



}
