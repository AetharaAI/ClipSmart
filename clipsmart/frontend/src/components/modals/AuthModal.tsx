'use client';

import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { X, Mail, Lock, User, Eye, EyeOff, Github } from 'lucide-react';
import { useAuthStore, useUIStore } from '@/lib/stores';
import { validateEmail, validatePassword } from '@/lib/utils';
import toast from 'react-hot-toast';

interface AuthModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export function AuthModal({ isOpen, onClose }: AuthModalProps) {
  const [isSignUp, setIsSignUp] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
    fullName: '',
  });
  const [errors, setErrors] = useState<Record<string, string>>({});

  const { login, register } = useAuthStore();

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    
    // Clear error when user starts typing
    if (errors[name]) {
      setErrors(prev => ({ ...prev, [name]: '' }));
    }
  };

  const validateForm = (): boolean => {
    const newErrors: Record<string, string> = {};

    // Email validation
    if (!formData.email) {
      newErrors.email = 'Email is required';
    } else if (!validateEmail(formData.email)) {
      newErrors.email = 'Please enter a valid email address';
    }

    // Password validation
    if (!formData.password) {
      newErrors.password = 'Password is required';
    } else if (isSignUp) {
      const passwordValidation = validatePassword(formData.password);
      if (!passwordValidation.valid) {
        newErrors.password = passwordValidation.errors[0];
      }
    }

    // Confirm password (only for sign up)
    if (isSignUp) {
      if (!formData.confirmPassword) {
        newErrors.confirmPassword = 'Please confirm your password';
      } else if (formData.password !== formData.confirmPassword) {
        newErrors.confirmPassword = 'Passwords do not match';
      }
    }

    // Full name (only for sign up)
    if (isSignUp && !formData.fullName) {
      newErrors.fullName = 'Full name is required';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }

    setIsLoading(true);

    try {
      if (isSignUp) {
        await register(formData.email, formData.password, formData.fullName);
        toast.success('Account created successfully!');
      } else {
        await login(formData.email, formData.password);
        toast.success('Welcome back!');
      }
      
      onClose();
    } catch (error: any) {
      toast.error(error.message || 'Authentication failed');
    } finally {
      setIsLoading(false);
    }
  };

  const handleGoogleAuth = async () => {
    try {
      // TODO: Implement Google OAuth
      toast.error('Google OAuth coming soon!');
    } catch (error: any) {
      toast.error('Google authentication failed');
    }
  };

  const handleGitHubAuth = async () => {
    try {
      // TODO: Implement GitHub OAuth
      toast.error('GitHub OAuth coming soon!');
    } catch (error: any) {
      toast.error('GitHub authentication failed');
    }
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <>
          {/* Backdrop */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-black/60 backdrop-blur-sm z-50"
          />

          {/* Modal */}
          <motion.div
            initial={{ opacity: 0, scale: 0.9, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.9, y: 20 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4"
          >
            <div className="w-full max-w-md bg-ethereal-800 border border-white/20 rounded-2xl shadow-2xl">
              {/* Header */}
              <div className="flex items-center justify-between p-6 border-b border-white/10">
                <div>
                  <h2 className="text-2xl font-bold text-white">
                    {isSignUp ? 'Create Account' : 'Welcome Back'}
                  </h2>
                  <p className="text-ethereal-400 mt-1">
                    {isSignUp 
                      ? 'Join thousands of content creators' 
                      : 'Sign in to your account'
                    }
                  </p>
                </div>
                <button
                  onClick={onClose}
                  className="p-2 hover:bg-white/10 rounded-lg transition-colors"
                >
                  <X className="w-5 h-5 text-ethereal-400" />
                </button>
              </div>

              {/* Form */}
              <form onSubmit={handleSubmit} className="p-6 space-y-4">
                {/* Full Name (Sign Up Only) */}
                {isSignUp && (
                  <div>
                    <label htmlFor="fullName" className="block text-sm font-medium text-ethereal-300 mb-2">
                      Full Name
                    </label>
                    <div className="relative">
                      <User className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-ethereal-400" />
                      <input
                        type="text"
                        id="fullName"
                        name="fullName"
                        value={formData.fullName}
                        onChange={handleInputChange}
                        className={`w-full pl-10 pr-4 py-3 bg-ethereal-700 border rounded-lg text-white placeholder-ethereal-500 focus:outline-none focus:ring-2 focus:ring-neon-500 transition-colors ${
                          errors.fullName ? 'border-red-500' : 'border-white/20'
                        }`}
                        placeholder="Enter your full name"
                      />
                    </div>
                    {errors.fullName && (
                      <p className="mt-1 text-sm text-red-400">{errors.fullName}</p>
                    )}
                  </div>
                )}

                {/* Email */}
                <div>
                  <label htmlFor="email" className="block text-sm font-medium text-ethereal-300 mb-2">
                    Email Address
                  </label>
                  <div className="relative">
                    <Mail className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-ethereal-400" />
                    <input
                      type="email"
                      id="email"
                      name="email"
                      value={formData.email}
                      onChange={handleInputChange}
                      className={`w-full pl-10 pr-4 py-3 bg-ethereal-700 border rounded-lg text-white placeholder-ethereal-500 focus:outline-none focus:ring-2 focus:ring-neon-500 transition-colors ${
                        errors.email ? 'border-red-500' : 'border-white/20'
                      }`}
                      placeholder="Enter your email"
                    />
                  </div>
                  {errors.email && (
                    <p className="mt-1 text-sm text-red-400">{errors.email}</p>
                  )}
                </div>

                {/* Password */}
                <div>
                  <label htmlFor="password" className="block text-sm font-medium text-ethereal-300 mb-2">
                    Password
                  </label>
                  <div className="relative">
                    <Lock className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-ethereal-400" />
                    <input
                      type={showPassword ? 'text' : 'password'}
                      id="password"
                      name="password"
                      value={formData.password}
                      onChange={handleInputChange}
                      className={`w-full pl-10 pr-12 py-3 bg-ethereal-700 border rounded-lg text-white placeholder-ethereal-500 focus:outline-none focus:ring-2 focus:ring-neon-500 transition-colors ${
                        errors.password ? 'border-red-500' : 'border-white/20'
                      }`}
                      placeholder="Enter your password"
                    />
                    <button
                      type="button"
                      onClick={() => setShowPassword(!showPassword)}
                      className="absolute right-3 top-1/2 transform -translate-y-1/2 text-ethereal-400 hover:text-white transition-colors"
                    >
                      {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                    </button>
                  </div>
                  {errors.password && (
                    <p className="mt-1 text-sm text-red-400">{errors.password}</p>
                  )}
                </div>

                {/* Confirm Password (Sign Up Only) */}
                {isSignUp && (
                  <div>
                    <label htmlFor="confirmPassword" className="block text-sm font-medium text-ethereal-300 mb-2">
                      Confirm Password
                    </label>
                    <div className="relative">
                      <Lock className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-ethereal-400" />
                      <input
                        type="password"
                        id="confirmPassword"
                        name="confirmPassword"
                        value={formData.confirmPassword}
                        onChange={handleInputChange}
                        className={`w-full pl-10 pr-4 py-3 bg-ethereal-700 border rounded-lg text-white placeholder-ethereal-500 focus:outline-none focus:ring-2 focus:ring-neon-500 transition-colors ${
                          errors.confirmPassword ? 'border-red-500' : 'border-white/20'
                        }`}
                        placeholder="Confirm your password"
                      />
                    </div>
                    {errors.confirmPassword && (
                      <p className="mt-1 text-sm text-red-400">{errors.confirmPassword}</p>
                    )}
                  </div>
                )}

                {/* Submit Button */}
                <button
                  type="submit"
                  disabled={isLoading}
                  className="w-full bg-neon-gradient hover:shadow-neon text-white font-semibold py-3 px-4 rounded-lg transition-all duration-300 transform hover:scale-105 disabled:opacity-50 disabled:transform-none"
                >
                  {isLoading ? (
                    <span className="flex items-center justify-center space-x-2">
                      <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                      <span>{isSignUp ? 'Creating Account...' : 'Signing In...'}</span>
                    </span>
                  ) : (
                    isSignUp ? 'Create Account' : 'Sign In'
                  )}
                </button>

                {/* Divider */}
                <div className="relative my-6">
                  <div className="absolute inset-0 flex items-center">
                    <div className="w-full border-t border-white/10" />
                  </div>
                  <div className="relative flex justify-center text-sm">
                    <span className="px-2 bg-ethereal-800 text-ethereal-400">Or continue with</span>
                  </div>
                </div>

                {/* OAuth Buttons */}
                <div className="grid grid-cols-2 gap-3">
                  <button
                    type="button"
                    onClick={handleGoogleAuth}
                    className="flex items-center justify-center space-x-2 py-3 px-4 bg-ethereal-700 border border-white/20 rounded-lg text-ethereal-300 hover:bg-white/10 transition-colors"
                  >
                    <span className="w-5 h-5">G</span>
                    <span className="text-sm font-medium">Google</span>
                  </button>

                  <button
                    type="button"
                    onClick={handleGitHubAuth}
                    className="flex items-center justify-center space-x-2 py-3 px-4 bg-ethereal-700 border border-white/20 rounded-lg text-ethereal-300 hover:bg-white/10 transition-colors"
                  >
                    <Github className="w-5 h-5" />
                    <span className="text-sm font-medium">GitHub</span>
                  </button>
                </div>
              </form>

              {/* Footer */}
              <div className="px-6 pb-6 text-center">
                <p className="text-ethereal-400 text-sm">
                  {isSignUp ? 'Already have an account?' : "Don't have an account?"}
                  <button
                    type="button"
                    onClick={() => {
                      setIsSignUp(!isSignUp);
                      setErrors({});
                      setFormData({
                        email: '',
                        password: '',
                        confirmPassword: '',
                        fullName: '',
                      });
                    }}
                    className="ml-1 text-neon-400 hover:text-neon-300 font-semibold transition-colors"
                  >
                    {isSignUp ? 'Sign In' : 'Sign Up'}
                  </button>
                </p>
              </div>
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}