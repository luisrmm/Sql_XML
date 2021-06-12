using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ClienteFactura
{
    public partial class Factura : Form
    {
        public ConectionToServer CtS
        { get; set; }

        public Factura(ConectionToServer info)
        {
            CtS = info;
            InitializeComponent();
        }

        private void btnFactura_Click(object sender, EventArgs e)
        {
            try
            {
                ConectionToServer info2 = CtS;
                JObject jsonObject = new JObject
                {
                    ["action"] = "getFactura",
                };

                string json1 = JsonConvert.SerializeObject(jsonObject, Formatting.Indented);


                info2.Data = json1;
                info2.Send();
                JObject json_data = info2.Receive();


                string datos = JsonConvert.SerializeObject(json_data, Formatting.Indented);

                Debug.WriteLine("Data : " + datos);


                Request request = JsonConvert.DeserializeObject<Request>(datos);

                if (request.status == 1)
                {

                  

                    string[] a = request.data;
                    string detalles = "";
                    for (int i = 0; i < a.Length; i++)
                    {
                        Debug.WriteLine(a[i]);
                        detalles = detalles + a[i] + "\n";
                    }

                    datosFacturatxt.Text = detalles;
                }
                else
                {
                    MessageBox.Show("Project id not found", "Information to the user",
                        MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
            catch (Exception error_)
            {
                Debug.WriteLine(error_);
                throw;
            }
        }
    }
}
