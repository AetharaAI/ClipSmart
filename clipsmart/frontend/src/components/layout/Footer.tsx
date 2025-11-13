'use client';

import Link from 'next/link';
import { motion } from 'framer-motion';
import { 
  Play, 
  Github, 
  Twitter, 
  Linkedin, 
  Mail,
  ExternalLink,
  Zap,
  Heart
} from 'lucide-react';

export function Footer() {
  const currentYear = new Date().getFullYear();

  const footerLinks = {
    product: [
      { name: 'Features', href: '#features' },
      { name: 'How It Works', href: '#how-it-works' },
      { name: 'Pricing', href: '#pricing' },
      { name: 'API Documentation', href: '/docs' },
    ],
    company: [
      { name: 'About Us', href: '/about' },
      { name: 'Blog', href: '/blog' },
      { name: 'Careers', href: '/careers' },
      { name: 'Press Kit', href: '/press' },
    ],
    support: [
      { name: 'Help Center', href: '/help' },
      { name: 'Contact Support', href: '/support' },
      { name: 'Status', href: '/status' },
      { name: 'Community', href: '/community' },
    ],
    legal: [
      { name: 'Privacy Policy', href: '/privacy' },
      { name: 'Terms of Service', href: '/terms' },
      { name: 'Cookie Policy', href: '/cookies' },
      { name: 'GDPR', href: '/gdpr' },
    ],
  };

  const socialLinks = [
    { name: 'GitHub', icon: Github, href: 'https://github.com/aetherpro' },
    { name: 'Twitter', icon: Twitter, href: 'https://twitter.com/aetherpro' },
    { name: 'LinkedIn', icon: Linkedin, href: 'https://linkedin.com/company/aetherpro' },
    { name: 'Email', icon: Mail, href: 'mailto:hello@aetherpro.com' },
  ];

  return (
    <footer className="bg-ethereal-950 border-t border-white/10">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        {/* Main Footer Content */}
        <div className="py-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-6 gap-8">
          {/* Brand Section */}
          <div className="lg:col-span-2">
            <Link href="/" className="flex items-center space-x-2 mb-4">
              <div className="w-10 h-10 bg-neon-gradient rounded-lg flex items-center justify-center">
                <Play className="w-6 h-6 text-white" />
              </div>
              <span className="text-2xl font-bold bg-neon-gradient bg-clip-text text-transparent">
                ClipSmart
              </span>
            </Link>
            
            <p className="text-ethereal-400 mb-6 max-w-sm">
              Transform long-form videos into viral-ready split-screen shorts with advanced AI analysis. 
              Powered by MiniMax-M2 for content creators and marketers.
            </p>
            
            {/* Tech Stack Badge */}
            <div className="flex items-center space-x-2 text-sm text-ethereal-500">
              <Zap className="w-4 h-4 text-neon-400" />
              <span>Powered by MiniMax-M2 AI</span>
            </div>
          </div>

          {/* Links Sections */}
          <div>
            <h3 className="text-white font-semibold mb-4">Product</h3>
            <ul className="space-y-3">
              {footerLinks.product.map((link) => (
                <li key={link.name}>
                  <Link
                    href={link.href}
                    className="text-ethereal-400 hover:text-white transition-colors"
                  >
                    {link.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="text-white font-semibold mb-4">Company</h3>
            <ul className="space-y-3">
              {footerLinks.company.map((link) => (
                <li key={link.name}>
                  <Link
                    href={link.href}
                    className="text-ethereal-400 hover:text-white transition-colors"
                  >
                    {link.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="text-white font-semibold mb-4">Support</h3>
            <ul className="space-y-3">
              {footerLinks.support.map((link) => (
                <li key={link.name}>
                  <Link
                    href={link.href}
                    className="text-ethereal-400 hover:text-white transition-colors"
                  >
                    {link.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="text-white font-semibold mb-4">Legal</h3>
            <ul className="space-y-3">
              {footerLinks.legal.map((link) => (
                <li key={link.name}>
                  <Link
                    href={link.href}
                    className="text-ethereal-400 hover:text-white transition-colors"
                  >
                    {link.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Newsletter Signup */}
        <div className="py-8 border-t border-white/10">
          <div className="max-w-md">
            <h3 className="text-white font-semibold mb-2">Stay Updated</h3>
            <p className="text-ethereal-400 mb-4 text-sm">
              Get the latest updates on new features and AI improvements.
            </p>
            <div className="flex space-x-2">
              <input
                type="email"
                placeholder="Enter your email"
                className="flex-1 px-3 py-2 bg-ethereal-800 border border-white/20 rounded-lg text-white placeholder-ethereal-500 focus:outline-none focus:ring-2 focus:ring-neon-500 focus:border-transparent"
              />
              <button className="btn-primary px-4 py-2 text-sm">
                Subscribe
              </button>
            </div>
          </div>
        </div>

        {/* Bottom Section */}
        <div className="py-6 border-t border-white/10 flex flex-col sm:flex-row justify-between items-center">
          <div className="flex items-center space-x-4 text-ethereal-400 text-sm">
            <span>© {currentYear} AetherPro Technologies LLC</span>
            <span>•</span>
            <span>All rights reserved</span>
          </div>

          {/* Social Links */}
          <div className="flex items-center space-x-4 mt-4 sm:mt-0">
            {socialLinks.map((social) => {
              const Icon = social.icon;
              return (
                <motion.a
                  key={social.name}
                  href={social.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  whileHover={{ scale: 1.1 }}
                  whileTap={{ scale: 0.95 }}
                  className="w-8 h-8 bg-ethereal-800 hover:bg-neon-600 rounded-lg flex items-center justify-center text-ethereal-400 hover:text-white transition-colors"
                  aria-label={social.name}
                >
                  <Icon className="w-4 h-4" />
                </motion.a>
              );
            })}
          </div>
        </div>

        {/* Aether Ecosystem Attribution */}
        <div className="py-4 border-t border-white/10 text-center">
          <div className="flex items-center justify-center space-x-2 text-ethereal-500 text-sm">
            <span>Part of the</span>
            <Link 
              href="https://aetherpro.com" 
              className="text-neon-400 hover:text-neon-300 transition-colors flex items-center space-x-1"
              target="_blank"
              rel="noopener noreferrer"
            >
              <span>AetherPro Ecosystem</span>
              <ExternalLink className="w-3 h-3" />
            </Link>
            <span>•</span>
            <span className="flex items-center space-x-1">
              <span>Made with</span>
              <Heart className="w-3 h-3 text-red-500" />
              <span>by MiniMax Agent</span>
            </span>
          </div>
        </div>
      </div>
    </footer>
  );
}