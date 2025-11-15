'use client';

import { motion } from 'framer-motion';
import { Star, Quote } from 'lucide-react';
import Image from 'next/image';

const testimonials = [
  {
    name: 'Sarah Chen',
    role: 'Content Creator',
    avatar: '👩‍💼',
    platform: 'TikTok',
    followers: '2.5M',
    rating: 5,
    quote: "ClipSmart cut my editing time by 90%. I went from spending 6 hours on a video to just 30 minutes. The AI knows exactly which moments will go viral."
  },
  {
    name: 'Marcus Rodriguez',
    role: 'YouTube Creator',
    avatar: '👨‍🎨',
    platform: 'YouTube Shorts',
    followers: '890K',
    rating: 5,
    quote: "The attention scoring is insane. My shorts now consistently hit 1M+ views. ClipSmart understands engagement better than I do."
  },
  {
    name: 'Emily Watson',
    role: 'Social Media Manager',
    avatar: '👩‍💻',
    platform: 'Instagram',
    followers: '1.2M',
    rating: 5,
    quote: "Managing 5 clients used to be overwhelming. Now I can turn one podcast into 20 viral shorts in minutes. This is a game-changer for agencies."
  },
  {
    name: 'David Kim',
    role: 'Podcast Host',
    avatar: '👨‍🚀',
    platform: 'Multi-Platform',
    followers: '500K',
    rating: 5,
    quote: "The semantic mode is perfect for educational content. It finds clips that flow together naturally. My audience retention went up 3x."
  },
  {
    name: 'Lisa Anderson',
    role: 'Brand Strategist',
    avatar: '👩‍🔬',
    platform: 'TikTok',
    followers: '3.1M',
    rating: 5,
    quote: "ROI on ClipSmart is incredible. We're getting 10x more engagement with half the production costs. The auto-captions alone save hours."
  },
  {
    name: 'James Foster',
    role: 'Video Editor',
    avatar: '👨‍🎤',
    platform: 'YouTube',
    followers: '1.8M',
    rating: 5,
    quote: "As a professional editor, I was skeptical. But the AI's clip selection is better than most human editors. I use it for all my clients now."
  }
];

export function TestimonialsSection() {
  return (
    <section className="relative py-24 px-4 bg-ethereal-900 overflow-hidden">
      {/* Background decoration */}
      <div className="absolute inset-0 opacity-5">
        <div className="absolute top-0 left-0 w-96 h-96 bg-neon-500 rounded-full filter blur-3xl" />
        <div className="absolute bottom-0 right-0 w-96 h-96 bg-purple-500 rounded-full filter blur-3xl" />
      </div>

      <div className="max-w-7xl mx-auto relative">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">
            Loved by <span className="text-neon-400">10,000+</span> Creators
          </h2>
          <p className="text-xl text-ethereal-300 max-w-3xl mx-auto">
            Join thousands of content creators who are transforming their workflow
          </p>
        </motion.div>

        {/* Testimonials Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {testimonials.map((testimonial, index) => (
            <motion.div
              key={testimonial.name}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              whileHover={{ y: -8, transition: { duration: 0.2 } }}
              className="group"
            >
              <div className="h-full p-6 rounded-2xl bg-ethereal-800/50 backdrop-blur-sm border border-ethereal-700 hover:border-neon-500/50 transition-all duration-300 relative">
                {/* Quote Icon */}
                <div className="absolute top-6 right-6 opacity-10 group-hover:opacity-20 transition-opacity">
                  <Quote className="w-16 h-16 text-neon-400" />
                </div>

                {/* Rating */}
                <div className="flex gap-1 mb-4">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <Star key={i} className="w-4 h-4 fill-yellow-400 text-yellow-400" />
                  ))}
                </div>

                {/* Quote */}
                <p className="text-ethereal-200 leading-relaxed mb-6 relative z-10">
                  "{testimonial.quote}"
                </p>

                {/* Author */}
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 rounded-full bg-gradient-to-br from-neon-500 to-purple-600 flex items-center justify-center text-2xl">
                    {testimonial.avatar}
                  </div>
                  <div>
                    <div className="font-bold text-white">
                      {testimonial.name}
                    </div>
                    <div className="text-sm text-ethereal-300">
                      {testimonial.role}
                    </div>
                    <div className="text-xs text-neon-400">
                      {testimonial.followers} followers • {testimonial.platform}
                    </div>
                  </div>
                </div>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Stats */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.6 }}
          className="mt-16 grid grid-cols-2 md:grid-cols-4 gap-8 max-w-4xl mx-auto"
        >
          {[
            { value: '10K+', label: 'Active Users' },
            { value: '2M+', label: 'Clips Generated' },
            { value: '4.9/5', label: 'Average Rating' },
            { value: '98%', label: 'Would Recommend' }
          ].map((stat, index) => (
            <div key={index} className="text-center">
              <div className="text-3xl md:text-4xl font-bold text-neon-400 mb-2">
                {stat.value}
              </div>
              <div className="text-sm text-ethereal-300">
                {stat.label}
              </div>
            </div>
          ))}
        </motion.div>
      </div>
    </section>
  );
}
