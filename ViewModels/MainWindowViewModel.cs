using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml;
using Avalonia.Styling;
using Avalonia.ReactiveUI;
using ReactiveUI;
using OpenCvSharp;

using System;
using System.IO;
using System.Diagnostics;
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
            string output = "output";

            if(Directory.Exists(output) == false)
            {
                try
                {
                    Directory.CreateDirectory(output);
                }
                catch(Exception e)
                {
                    ShowMessage($"ERROR. {e}");
                    return;
                }
            }

            Mat img;

            try
            {
                img = Cv2.ImRead(path, ImreadModes.Unchanged); // Open image
                img.Resize(OpenCvSharp.Size.Zero, scale, scale, InterpolationFlags.Nearest); // Resize image
            }
            catch(Exception e)
            {
                ShowMessage($"ERROR. {e}");
                return;
            }

            try
            {
                img.ImWrite(output + "/" + "img.png"); // Save image to file
            }
            catch(Exception e)
            {
                ShowMessage($"ERROR. {e}");
            }

            img.Dispose(); // Clear memory
        }

        public void ShowMessage(string message, string title = "GPAS")
        {
            var messageBox = MessageBox.Avalonia.MessageBoxManager
                .GetMessageBoxStandardWindow(title, message);
            messageBox.Show();
        }

        public void OpenOutputFolder()
        {
            try
            {
                Process.Start(@"output");
            }
            catch(Exception e)
            {
                ShowMessage($"ERROR. {e}");
            }
        }

        public void OnOpenFile()
        {
            ResizeImage("input/sprite1.png");
        }

        public void OnOpenFolder()
        {
            ShowMessage("Open folder");
        }

        public void OnCopyFromCb()
        {
            ShowMessage("Copy from clipboard");
        }
    }
}
