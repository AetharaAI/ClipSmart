'use client';

import { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Play, 
  Upload, 
  Library, 
  Settings, 
  User, 
  LogOut, 
  Menu,
  X,
  Zap,
  Sparkles
} from 'lucide-react';
import { useAuthStore, useUIStore } from '@/lib/stores';
import { cn } from '@/lib/utils';

export function Navbar() {
  const [isOpen, setIsOpen] = useState(false);
  const pathname = usePathname();
  const { user, isAuthenticated, logout } = useAuthStore();
  const { theme, toggleTheme, openModal } = useUIStore();

  const navigation = [
    { name: 'Upload', href: '/upload', icon: Upload },
    { name: 'Library', href: '/library', icon: Library },
    { name: 'Analyze', href: '/analyze', icon: Zap },
  ];

  const handleAuthAction = () => {
    if (isAuthenticated) {
      logout();
    } else {
      openModal('settings'); // This will open auth modal
    }
  };

  return (
    <motion.nav
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      className="fixed top-0 left-0 right-0 z-50 bg-glass border-b border-white/10 backdrop-blur-xl"
    >
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 items-center justify-between">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-2 group">
            <div className="relative">
              <motion.div
                whileHover={{ scale: 1.05, rotate: 5 }}
                className="flex items-center justify-center w-10 h-10 bg-neon-gradient rounded-lg"
              >
                <Play className="w-6 h-6 text-white" />
              </motion.div>
              <motion.div
                animate={{ scale: [1, 1.2, 1] }}
                transition={{ repeat: Infinity, duration: 2 }}
                className="absolute -top-1 -right-1 w-3 h-3 bg-green-400 rounded-full"
              />
            </div>
            <div className="hidden sm:block">
              <span className="text-xl font-bold bg-neon-gradient bg-clip-text text-transparent">
                ClipSmart
              </span>
              <div className="text-xs text-ethereal-400 flex items-center gap-1">
                <Sparkles className="w-3 h-3" />
                Powered by MiniMax-M2
              </div>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-8">
            {navigation.map((item) => {
              const isActive = pathname === item.href;
              const Icon = item.icon;
              
              return (
                <Link
                  key={item.name}
                  href={item.href}
                  className={cn(
                    'flex items-center space-x-2 px-3 py-2 rounded-lg text-sm font-medium transition-all duration-200',
                    isActive
                      ? 'bg-neon-600 text-white shadow-neon'
                      : 'text-ethereal-300 hover:text-white hover:bg-white/10'
                  )}
                >
                  <Icon className="w-4 h-4" />
                  <span>{item.name}</span>
                </Link>
              );
            })}
          </div>

          {/* Right side actions */}
          <div className="flex items-center space-x-4">
            {/* Theme Toggle */}
            <button
              onClick={toggleTheme}
              className="p-2 rounded-lg bg-white/10 hover:bg-white/20 transition-colors"
              aria-label="Toggle theme"
            >
              {theme === 'dark' ? '🌙' : '☀️'}
            </button>

            {/* User Menu */}
            {isAuthenticated ? (
              <div className="relative">
                <button
                  className="flex items-center space-x-2 p-2 rounded-lg bg-white/10 hover:bg-white/20 transition-colors"
                  onClick={() => setIsOpen(!isOpen)}
                >
                  {user?.avatar_url ? (
                    <img
                      src={user.avatar_url}
                      alt={user.full_name || 'User'}
                      className="w-8 h-8 rounded-full"
                    />
                  ) : (
                    <div className="w-8 h-8 bg-neon-600 rounded-full flex items-center justify-center">
                      <User className="w-4 h-4 text-white" />
                    </div>
                  )}
                  <span className="hidden sm:block text-sm font-medium">
                    {user?.full_name || 'User'}
                  </span>
                </button>

                {/* Dropdown Menu */}
                <AnimatePresence>
                  {isOpen && (
                    <motion.div
                      initial={{ opacity: 0, scale: 0.95, y: -10 }}
                      animate={{ opacity: 1, scale: 1, y: 0 }}
                      exit={{ opacity: 0, scale: 0.95, y: -10 }}
                      className="absolute right-0 mt-2 w-48 bg-ethereal-800 border border-white/20 rounded-lg shadow-xl py-2"
                    >
                      <Link
                        href="/profile"
                        className="flex items-center space-x-2 px-4 py-2 text-sm hover:bg-white/10 transition-colors"
                        onClick={() => setIsOpen(false)}
                      >
                        <User className="w-4 h-4" />
                        <span>Profile</span>
                      </Link>
                      <Link
                        href="/settings"
                        className="flex items-center space-x-2 px-4 py-2 text-sm hover:bg-white/10 transition-colors"
                        onClick={() => setIsOpen(false)}
                      >
                        <Settings className="w-4 h-4" />
                        <span>Settings</span>
                      </Link>
                      <hr className="my-2 border-white/20" />
                      <button
                        onClick={() => {
                          handleAuthAction();
                          setIsOpen(false);
                        }}
                        className="flex items-center space-x-2 w-full px-4 py-2 text-sm text-red-400 hover:bg-red-500/20 transition-colors"
                      >
                        <LogOut className="w-4 h-4" />
                        <span>Sign Out</span>
                      </button>
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>
            ) : (
              <Link
                href="/auth"
                className="btn-primary"
              >
                Sign In
              </Link>
            )}

            {/* Mobile Menu Button */}
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="md:hidden p-2 rounded-lg bg-white/10 hover:bg-white/20 transition-colors"
              aria-label="Toggle menu"
            >
              {isOpen ? (
                <X className="w-5 h-5" />
              ) : (
                <Menu className="w-5 h-5" />
              )}
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        <AnimatePresence>
          {isOpen && (
            <motion.div
              initial={{ height: 0, opacity: 0 }}
              animate={{ height: 'auto', opacity: 1 }}
              exit={{ height: 0, opacity: 0 }}
              className="md:hidden overflow-hidden border-t border-white/10"
            >
              <div className="py-4 space-y-2">
                {navigation.map((item) => {
                  const isActive = pathname === item.href;
                  const Icon = item.icon;
                  
                  return (
                    <Link
                      key={item.name}
                      href={item.href}
                      className={cn(
                        'flex items-center space-x-3 px-4 py-3 rounded-lg text-sm font-medium transition-all duration-200',
                        isActive
                          ? 'bg-neon-600 text-white'
                          : 'text-ethereal-300 hover:text-white hover:bg-white/10'
                      )}
                      onClick={() => setIsOpen(false)}
                    >
                      <Icon className="w-5 h-5" />
                      <span>{item.name}</span>
                    </Link>
                  );
                })}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </motion.nav>
  );
}