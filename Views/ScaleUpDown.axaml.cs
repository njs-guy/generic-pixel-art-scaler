using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml;

namespace GenericPixelArtScaler.Views
{
    public partial class ScaleUpDown : UserControl
    {
        public ScaleUpDown()
        {
            InitializeComponent();
        }

        private void InitializeComponent()
        {
            AvaloniaXamlLoader.Load(this);
        }
    }
}
