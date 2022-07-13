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
using System.Runtime.InteropServices; // Check OS

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

            if(CheckOutputFolder() == false)
            {
                return; // Cannot write to output, do nothing.
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

        // Checks if there is an output directory. If not, creates it.
        public bool CheckOutputFolder()
        {
            //bool result = false;
            string path = "output";

            if (Directory.Exists(path) == false)
            {
                try
                {
                    Directory.CreateDirectory(path);
                    return true;
                }
                catch (Exception e)
                {
                    ShowMessage($"ERROR. {e}");
                    return false;
                }
            }
            else
            {
                return true;
            }
        }

        public void OpenOutputFolder()
        {
            if (CheckOutputFolder() == false)
            {
                return; // Cannot write to output. Do nothing.
            }

            try
            {   
                if(RuntimeInformation.IsOSPlatform(OSPlatform.Windows)) // If on Windows
                {
                    Process.Start("explorer.exe", @"output");
                    return;
                }

                if(RuntimeInformation.IsOSPlatform(OSPlatform.Linux)) // If on Linux
                {
                    ShowMessage("You are on Linux. The default file explorer is supposed to open but I haven't made that yet.");
                    return;
                }

                if(RuntimeInformation.IsOSPlatform(OSPlatform.OSX)) // If on Mac
                {
                    ShowMessage("You are on Mac OSX. The default file explorer is supposed to open but I don't have a Mac to test this. If you want to add this yourself, contributions are welcome!");
                    return;
                }
            }
            catch(Exception e)
            {
                ShowMessage($"ERROR. {e}");
            }
        }

        public void OnOpenFile()
        {
            ResizeImage("input/sprite1.png");
            OpenOutputFolder();
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
