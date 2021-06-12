using System;
using System.Collections.Generic;
using System.Text;

namespace ClienteFactura
{
    class Request
    {
        public int status;
        public string[] data;
        public string message;
        public string[][] dataMatrix;


        public Request(int status, string[] data, string message, string[][] dataMatrix)
        {
            this.status = status;
            this.data = data;
            this.message = message;
            this.dataMatrix = dataMatrix;

        }
    }
}
