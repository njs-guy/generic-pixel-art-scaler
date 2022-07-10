using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml;
using Avalonia.ReactiveUI;
using ReactiveUI;

using System;
using System.Collections.Generic;
using System.Text;
using System.Windows.Input;

using GenericPixelArtScaler.Views;

namespace GenericPixelArtScaler.ViewModels
{
    public class MainWindowViewModel : ReactiveWindow<MainWindowViewModel>
    {
        public Interaction<AboutWindow, MenuStrip?> OpenAbout { get; }
        public string Greeting => "Welcome to Avalonia!";

        public MainWindowViewModel()
        {
            OpenAbout = new Interaction<AboutWindow, MenuStrip?>();

        }

        public void OpenAboutWindow()
        {
            var aboutWindow = new AboutWindow();
            aboutWindow.Show();
        }

        public void ShowSource()
        {
            Console.WriteLine("Wow");
        }
    }
}
