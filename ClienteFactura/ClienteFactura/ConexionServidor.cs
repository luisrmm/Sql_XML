using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Windows.Forms;

namespace ClienteFactura
{
    public class ConectionToServer
    {

        public string Data
        { get; set; }

        public JObject Recibido
        { get; set; }

        public Socket Listen
        { get; set; }

        public void Init()
        {
            try
            {
                Listen = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                IPEndPoint connect = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 8000);

                Listen.Connect(connect);

            }
            catch (Exception error_)
            {
                MessageBox.Show("Server Down", "Connetion Failure", MessageBoxButtons.OK, MessageBoxIcon.Warning);

                Debug.WriteLine(error_);
                throw;
            }
        }


        public void Send()
        {
            try
            {
                byte[] enviar_info = new byte[2048];

                enviar_info = Encoding.Default.GetBytes(Data);

                this.Listen.Send(enviar_info);

            }
            catch (Exception error_)
            {
                Debug.WriteLine(error_);
                throw;
            }

        }


        public JObject Receive()
        {

            try
            {
                byte[] data = new byte[2048];
                int receivedDataLength = Listen.Receive(data);
                string stringData = Encoding.ASCII.GetString(data, 0, receivedDataLength);

                JObject json_data = JObject.Parse(stringData);

                return json_data;
            }
            catch (Exception error_)
            {
                Debug.WriteLine(error_);
                throw;
            }
        }
    }
}
