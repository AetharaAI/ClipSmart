'use client';

import { motion } from 'framer-motion';
import { ArrowRight, Sparkles, Zap } from 'lucide-react';

interface CTASectionProps {
  onGetStarted: () => void;
}

export function CTASection({ onGetStarted }: CTASectionProps) {
  return (
    <section className="relative py-24 px-4 bg-gradient-to-br from-neon-900 via-purple-900 to-ethereal-900 overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0">
        <div className="absolute inset-0 bg-gradient-to-br from-neon-500/10 via-purple-500/10 to-transparent" />

        {/* Floating particles */}
        {[...Array(20)].map((_, i) => (
          <motion.div
            key={i}
            className="absolute w-2 h-2 bg-neon-400 rounded-full"
            initial={{
              x: Math.random() * window.innerWidth,
              y: Math.random() * 600,
              opacity: 0.3,
            }}
            animate={{
              y: [null, Math.random() * -200, Math.random() * 600],
              opacity: [0.3, 0.8, 0.3],
            }}
            transition={{
              duration: Math.random() * 5 + 5,
              repeat: Infinity,
              ease: 'linear',
            }}
          />
        ))}
      </div>

      <div className="max-w-4xl mx-auto relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center"
        >
          {/* Icon */}
          <motion.div
            animate={{
              rotate: [0, 5, -5, 0],
              scale: [1, 1.1, 1],
            }}
            transition={{
              duration: 3,
              repeat: Infinity,
              ease: 'easeInOut',
            }}
            className="inline-block mb-8"
          >
            <div className="w-20 h-20 mx-auto rounded-2xl bg-gradient-to-br from-neon-500 to-purple-600 flex items-center justify-center shadow-2xl shadow-neon-500/50">
              <Sparkles className="w-10 h-10 text-white" />
            </div>
          </motion.div>

          {/* Headline */}
          <h2 className="text-4xl md:text-6xl font-bold text-white mb-6">
            Ready to Go <span className="text-neon-400">Viral</span>?
          </h2>

          <p className="text-xl md:text-2xl text-ethereal-200 mb-8 max-w-2xl mx-auto">
            Join 10,000+ creators using AI to transform their content into viral shorts
          </p>

          {/* Features List */}
          <div className="flex flex-wrap justify-center gap-4 mb-12">
            {[
              'No credit card required',
              '10 free videos',
              'Cancel anytime',
              '14-day money back'
            ].map((feature, index) => (
              <motion.div
                key={feature}
                initial={{ opacity: 0, scale: 0.8 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.3, delay: index * 0.1 }}
                className="flex items-center gap-2 px-4 py-2 rounded-full bg-ethereal-800/50 backdrop-blur-sm border border-ethereal-700"
              >
                <Zap className="w-4 h-4 text-neon-400" />
                <span className="text-sm text-ethereal-200">{feature}</span>
              </motion.div>
            ))}
          </div>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <motion.button
              onClick={onGetStarted}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="group px-8 py-4 bg-gradient-to-r from-neon-500 to-purple-600 text-white font-bold rounded-lg shadow-2xl shadow-neon-500/50 hover:shadow-neon-500/70 transition-all duration-300 flex items-center gap-2"
            >
              Start Creating for Free
              <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </motion.button>

            <motion.a
              href="#pricing"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="px-8 py-4 bg-ethereal-800/80 backdrop-blur-sm text-white font-bold rounded-lg border-2 border-ethereal-600 hover:border-neon-500/50 transition-all duration-300"
            >
              View Pricing
            </motion.a>
          </div>

          {/* Trust Indicators */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.4 }}
            className="mt-12 pt-8 border-t border-ethereal-700"
          >
            <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
              {[
                { value: '10K+', label: 'Active Creators' },
                { value: '2M+', label: 'Clips Generated' },
                { value: '4.9/5', label: 'User Rating' },
                { value: '90%', label: 'Time Saved' }
              ].map((stat, index) => (
                <div key={index} className="text-center">
                  <div className="text-2xl md:text-3xl font-bold text-neon-400 mb-1">
                    {stat.value}
                  </div>
                  <div className="text-sm text-ethereal-300">
                    {stat.label}
                  </div>
                </div>
              ))}
            </div>
          </motion.div>
        </motion.div>
      </div>
    </section>
  );
}
