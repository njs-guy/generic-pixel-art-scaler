using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml;

namespace GenericPixelArtScaler.Views
{
    public partial class MenuStrip : UserControl
    {
        public MenuStrip()
        {
            InitializeComponent();
        }

        private void InitializeComponent()
        {
            AvaloniaXamlLoader.Load(this);
        }
    }
}
