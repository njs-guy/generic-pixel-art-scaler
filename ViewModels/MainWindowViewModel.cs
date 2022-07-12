using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml;
using Avalonia.Styling;
using Avalonia.ReactiveUI;
using ReactiveUI;
using OpenCvSharp;

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
        public bool darkMode = true;

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
            System.Diagnostics.Process.Start(new System.Diagnostics.ProcessStartInfo
            {
                FileName = "https://github.com/njshockey/generic-pixel-art-scaler",
                UseShellExecute = true
            });
        }

        public void ExitApp()
        {
            System.Environment.Exit(0);
        }

        public void ResizeImage(string path, int scale = 2)
        {
            Mat img = Cv2.ImRead(path, ImreadModes.Unchanged);
        }

        public void showMessage(string message, string title = "GPAS")
        {
            var messageBox = MessageBox.Avalonia.MessageBoxManager
                .GetMessageBoxStandardWindow(title, message);
            messageBox.Show();
        }

        public void OnOpenFile()
        {
            showMessage("Open file");
        }

        public void OnOpenFolder()
        {
            showMessage("Open folder");
        }

        public void OnCopyFromCb()
        {
            showMessage("Copy from clipboard");
        }
    }
}
