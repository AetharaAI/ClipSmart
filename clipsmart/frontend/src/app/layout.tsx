import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import { Providers } from './providers';
import { Navbar } from '@/components/layout/Navbar';
import { Footer } from '@/components/layout/Footer';
import { Toaster } from 'react-hot-toast';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'ClipSmart - AI-Powered Video Content Creation Platform',
  description: 'Transform long-form videos into viral-ready split-screen shorts with advanced AI analysis. Powered by MiniMax-M2 for content creators and marketers.',
  keywords: 'video editing, AI video, content creation, social media, TikTok, YouTube Shorts, viral content, split-screen, AetherPro',
  authors: [{ name: 'AetherPro Technologies LLC' }],
  creator: 'AetherPro Technologies LLC',
  publisher: 'AetherPro Technologies LLC',
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: process.env.NEXT_PUBLIC_APP_URL || 'https://clipsmart.aetherpro.com',
    title: 'ClipSmart - AI-Powered Video Content Creation Platform',
    description: 'Transform long-form videos into viral-ready split-screen shorts with advanced AI analysis.',
    siteName: 'ClipSmart',
    images: [
      {
        url: '/og-image.jpg',
        width: 1200,
        height: 630,
        alt: 'ClipSmart - AI-Powered Video Content Creation',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'ClipSmart - AI-Powered Video Content Creation Platform',
    description: 'Transform long-form videos into viral-ready split-screen shorts with advanced AI analysis.',
    images: ['/og-image.jpg'],
    creator: '@aetherpro',
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  verification: {
    google: 'google-site-verification-code',
    yandex: 'yandex-verification-code',
    yahoo: 'yahoo-verification-code',
  },
  category: 'technology',
  classification: 'AI-powered video editing platform, content creation tools, social media automation',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={inter.className} suppressHydrationWarning>
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="theme-color" content="#0f172a" />
        <meta name="color-scheme" content="dark light" />
        <link rel="icon" href="/favicon.ico" />
        <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
        <link rel="manifest" href="/manifest.json" />
        <meta name="msapplication-TileColor" content="#0f172a" />
        <meta name="msapplication-TileImage" content="/mstile-144x144.png" />
      </head>
      <body className="min-h-screen bg-gradient-to-br from-ethereal-900 via-ethereal-800 to-ethereal-900 text-white antialiased">
        <Providers>
          <div className="relative flex min-h-screen flex-col">
            <Navbar />
            <main className="flex-1">
              {children}
            </main>
            <Footer />
          </div>
          <Toaster
            position="top-right"
            toastOptions={{
              duration: 4000,
              style: {
                background: 'rgba(15, 23, 42, 0.9)',
                color: 'white',
                border: '1px solid rgba(168, 85, 247, 0.3)',
                backdropFilter: 'blur(10px)',
              },
              success: {
                iconTheme: {
                  primary: '#10b981',
                  secondary: 'white',
                },
              },
              error: {
                iconTheme: {
                  primary: '#ef4444',
                  secondary: 'white',
                },
              },
            }}
          />
        </Providers>
      </body>
    </html>
  );
}