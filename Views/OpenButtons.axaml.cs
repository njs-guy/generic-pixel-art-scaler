using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml;

namespace GenericPixelArtScaler.Views
{
    public partial class OpenButtons : UserControl
    {
        public OpenButtons()
        {
            InitializeComponent();
        }

        private void InitializeComponent()
        {
            AvaloniaXamlLoader.Load(this);
        }
    }
}
